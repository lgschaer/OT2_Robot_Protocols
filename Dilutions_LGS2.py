### This protocol is for the Opentrons Robot. This script will transfer DNA samples from 2ml ependorf tubes at a 1:10 dil

from opentrons import labware, instruments

p200rack = labware.load('tiprack-200ul', '11')
p10rack = labware.load('tiprack-10ul','10')
tubes4 = labware.load('tube-rack-2ml', '4')
tubes5 = labware.load('tube-rack-2ml','5')
tubes1 = labware.load('tube-rack-2ml','1')
tubes2 = labware.load('tube-rack-2ml','2')

plate = labware.load('96-PCR-flat', '3')
trough = labware.load('trough-12row','6')

p50 = instruments.P10_Single(
    mount="left",
    tip_racks=[p10rack])#

p300 = instruments.P300_Single(
    mount='right',
    tip_racks=[p200rack])#

#Assigning well distribution locations, split into two due to 2 master mix tubes

water =trough.wells('A1')
platefill = plate.cols('1', to = '12')

wellsA = plate.wells('A1', 'A2', 'A3', 'A4', 'A5', 'A6',
                     'B1', 'B2', 'B3', 'B4', 'B5', 'B6',
                     'C1', 'C2', 'C3', 'C4', 'C5', 'C6',
                     'D1', 'D2', 'D3', 'D4', 'D5', 'D6')
wellsC = plate.wells('E1', 'E2', 'E3', 'E4', 'E5', 'E6',
                     'F1', 'F2', 'F3', 'F4', 'F5', 'F6',
                     'G1', 'G2', 'G3', 'G4', 'G5', 'G6',
                     'H1', 'H2', 'H3', 'H4', 'H5', 'H6')
wellsB = plate.wells('A7', 'A8', 'A9', 'A10', 'A11', 'A12',
                     'B7', 'B8', 'B9', 'B10', 'B11', 'B12',
                     'C7', 'C8', 'C9', 'C10', 'C11', 'C12',
                     'D7', 'D8', 'D9', 'D10', 'D11', 'D12')
wellsD = plate.wells('E7', 'E8', 'E9', 'E10', 'E11', 'E12',
                     'F7', 'F8', 'F9', 'F10', 'F11', 'F12',
                     'G7', 'G8', 'G9', 'G10', 'G11', 'G12',
                     'H7', 'H8', 'H9', 'H10', 'H11', 'H12')

tubesA = tubes4.wells('A1', 'A2', 'A3', 'A4', 'A5', 'A6',
                     'B1', 'B2', 'B3', 'B4', 'B5', 'B6',
                     'C1', 'C2', 'C3', 'C4', 'C5', 'C6',
                     'D1', 'D2', 'D3', 'D4', 'D5', 'D6')
tubesB = tubes5.wells('A1', 'A2', 'A3', 'A4', 'A5', 'A6',
                     'B1', 'B2', 'B3', 'B4', 'B5', 'B6',
                     'C1', 'C2', 'C3', 'C4', 'C5', 'C6',
                     'D1', 'D2', 'D3', 'D4', 'D5', 'D6')
tubesC = tubes1.wells('A1', 'A2', 'A3', 'A4', 'A5', 'A6',
                     'B1', 'B2', 'B3', 'B4', 'B5', 'B6',
                     'C1', 'C2', 'C3', 'C4', 'C5', 'C6',
                     'D1', 'D2', 'D3', 'D4', 'D5', 'D6')
tubesD = tubes2.wells('A1', 'A2', 'A3', 'A4', 'A5', 'A6',
                     'B1', 'B2', 'B3', 'B4', 'B5', 'B6',
                     'C1', 'C2', 'C3', 'C4', 'C5', 'C6',
                     'D1', 'D2', 'D3', 'D4', 'D5', 'D6')


# dispense from tube to plate, for all tubes
p50.transfer(
        5,
        tubesA,
        wellsA,
        new_tip='always',
        touch_tip=True
    )

p50.transfer(
        5,
        tubesB,
        wellsB,
        new_tip='always',
        touch_tip=True
    )

p50.transfer(
        5,
        tubesC,
        wellsC,
        new_tip='always',
        touch_tip=True
    )

p50.transfer(
        5,
        tubesD,
        wellsD,
        new_tip='always',
        touch_tip=True
    )

p300.transfer(
        50,
        water,
        platefill,
        mix_after = (3, 50),
        new_tip='always',
        touch_tip=True)


