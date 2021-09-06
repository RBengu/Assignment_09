#------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
#------------------------------------------#

import ProcessingClasses as PC
import IOClasses as IO

lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)

while True:
    IO.ScreenIO.print_menu()
    strChoice = IO.ScreenIO.menu_choice()

    if strChoice == 'x':
        break
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            try:
                lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
                IO.ScreenIO.show_inventory(lstOfCDObjects)
            except FileNotFoundError as e:
                print('File does not currently exist!', e, e.__doc__, type(e), sep='\n')
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'a':
        tplCdInfo = IO.ScreenIO.get_CD_info()
        PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'd':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'c':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        cd_idx = int(input('Select the CD / Album index: '))
        cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)
        while True:
            print('Tracks:')
            IO.ScreenIO.show_tracks(cd)
            IO.ScreenIO.print_CD_menu()
            # print('selection in sub menu: {}'.format(IO.ScreenIO.menu_CD_choice()))
            strChoice = IO.ScreenIO.menu_CD_choice()
            if strChoice == 'x':
                print('Returning to main menu.')
                break
            elif strChoice == 'a':
                tplTrackInfo = IO.ScreenIO.get_track_info()
                PC.DataProcessor.add_track(tplTrackInfo, cd)
                IO.ScreenIO.show_tracks(cd)
            elif strChoice == 'r':
                track_idx = int(input('Select the Track index to remove: '))
                cd.rmv_track(track_idx)
                IO.ScreenIO.show_tracks(cd)
            elif strChoice == 'd':
                print('Tracks:')
                IO.ScreenIO.show_tracks(cd)
            else:
                print('Returning to main menu.')
                break
    elif strChoice == 's':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:
        print('General Error')