'''
Plato Bot
Copyright © 2025, Quira Walker. All Rights Reserved.
This Code is licensed under the "GNU AGPL" License, a copy of this license is contained in this Folder.
If you did not receive a copy, you may find it at: https://www.gnu.org/licenses/agpl-3.0.html
'''
from Settings.botSettings import serverNode

practiceLog = {
    'Start'       : False,
    'Category'    : None,
    'Chord Count' : None,
    'Chords'      : None,
    'End'         : False,
    'Continue'    : None,
    'Timeout'     : False,
    'Stop'        : False
}
practiceMenuOptions = ['1','2']
delay               = 10        # Seconds

##USE ON MASTER##
masterChords = {
    'A':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/A.png',
    'A5':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/A5.png',
    'A13sus4':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/A13sus4.png',
    'A#5':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/A#5.png',
    'Ab5':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/Ab5.png',
    'Ab7':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/Ab7.png',
    'Ab9':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/Ab9.png',
    'Abdim':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/Abdim.png',
    'A#dim':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/A#dim.png',
    'Am':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/Am.png',
    'Am13':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/Am13.png',

    'B':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/B.png',
    'B5':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/B5.png',
    'B7':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/B7.png',
    'Bb':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/Bb.png',
    'Bb5':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/Bb5.png',
    'Bb7':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/Bb7.png',
    'Bb7sus4':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/Bb7sus4.png',
    'Bb13sus4':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/Bb13sus4.png',
    'Bbdim7':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/Bbdim7.png',
    'Bbm':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/Bbm.png',
    'Bbm7':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/Bbm7.png',
    'Bm':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/Bm.png',
    'Bm13':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/Bm13.png',

    'C':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/C.png',
    'C5':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/C5.png',
    'C#':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/C#.png',
    'C#+':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/C#+.png',
    'C#dim':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/C#dim.png',
    'C#m':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/C#m.png',
    'C#m7':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/C#m7.png',
    'Csus2':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/Csus2.png',

    'D':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/D.png',
    'D11':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/D11.png',
    'D#':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/D#.png',
    'Db':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/Db.png',
    'D#m':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/D#m.png',
    'Dm':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/Dm.png',
    'Dsus2':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/Dsus2.png',

    'E':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/E.png',
    'E5':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/E5.png',
    'Eb':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/Eb.png',
    'Em':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/Em.png',

    'F':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/F.png',
    'F#':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/F#.png',
    'F#m':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/F#m.png',
    'F#maj7':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/F#maj7.png',
    'Fmaj7':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/Fmaj7.png',

    'G':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/G.png',
    'G#':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/G#.png',
    'G#+':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/G#+.png',
    'Gb+':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/Gb+.png',
    'G#m':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/G#m.png',
    'Gm':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/Gm.png',

    'End':'/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/Supplement_Data/Chords/end.jpg'
    }

if serverNode == 'Master':
    CHORDS = masterChords