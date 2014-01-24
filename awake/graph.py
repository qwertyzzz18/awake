# This file is part of Awake - GB decompiler.
# Copyright (C) 2012  Wojciech Marczenko (devdri) <wojtek.marczenko@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from collections import defaultdict
from PIL import Image
from awake import address

def addr_symbol(addr):
    return 'A' + str(addr).replace(':', '_')

def save_dot(database, procs):
    with open('data/graph.dot', 'w') as f:
        f.write("""
digraph crossref {
    splines=line
    //concentrate=true
    rankdir=LR
    1->2->3
    
    { rank=same; A0000_1F54 }
    subgraph clusterInterrupts {
        label="Interrupts";
        { A0000_0000, A0000_0008, A0000_0010, A0000_0018, A0000_0020, A0000_0028, A0000_0030, A0000_0040, A0000_0048}
        { A0000_0050, A0000_0058, A0000_0060, A0000_2024, A0000_0038, A0000_2125, A0000_2306, A0000_1D57, A0000_1DE1}
        { A0000_1D01, A0000_1E5E, A0000_1E02, A0000_1EBE, A0001_4B0F, A0000_28CB, A0000_015F, A0001_4BD1, A0000_1D9E}
        { A0000_1D42, A0000_008D }
    }
    subgraph clusterOverworldLoop {
        label="Overworld Loop";
        { A0000_03FF, A0000_0402, A0000_0683, A0000_06A0, A0000_08E9, A0000_0B23, A0000_0C2A}
        { A0000_0BD1, A0000_0D27, A0000_0F4D, A0000_0FB7, A0000_0965}
        { A0000_039E, A0000_3EB5, A0000_0E65, A0000_0E6F, A0000_0E79, A0000_0E85, A0000_0E91, A0000_0EB2, A0000_0ED3}
        { A0000_0F08, A0000_0B6B, A0000_0C10, A0000_0B6D, A0000_08C9, A0000_08E1, A0000_098F, A0000_3EDD}
        { A0011_69A0, A0000_3EEA, A0000_12DA}
        { A0000_0EA6, A0000_0EF2, A0000_07B5, A0000_30FD, A0000_0F1D}
        }
    subgraph clusterMap {
        label="Map";
        { A0000_101B, A0000_3071, A0000_107C, A0000_3160, A0000_12BC, A0000_09FC, A0000_1238, A0000_07BA, A0000_1241}
        { A0000_0CAA, A0000_03A6, A0000_091F, A0000_310E, A0000_0ADE, A0000_0B02, A0000_3146, A0000_12E7}
        subgraph clusterMapWarp {
            label="Warps";
            { A0000_08E9, A0000_1313, A0000_06B4, A0000_06CC, A0000_0706, A0000_072F, A0000_0730, A0000_0735}
            { A0000_073C}
        }
    }
    subgraph clusterText {
        label="Text";
        { A0000_1956, A0000_1B0A, A0000_1AB4, A0000_1AD5, A0000_19F9, A0000_19FF, A0000_1A1D, A0000_1A11, A0000_1A17}
        { A0000_1A0B, A0000_1A05, A0000_1A7C, A0000_1A23, A0000_1AAD, A0000_1A95, A0000_1A29, A0000_1A91, A0000_1A2F}
        { A0000_1A35, A0000_3C49, A0000_1A4B, A0000_1B55, A0000_1B8A, A0000_1B78, A0000_1B97, A0000_1BA5, A0000_1BB7}
        { A0000_1BC5, A0000_1BCC, A0000_1BE7, A0000_1BFF, A0000_1C1D, A0000_1C31, A0000_1C78, A0000_1C9A, A0000_1CA3}
        { A0000_1955, A0000_29E8, A0000_194F, A0000_3C5F, A0000_3D89, A0000_3D83, A0000_3D25, A0000_15CD, A0000_1604}
        { A0000_2920, A0000_2ACD, A0000_2A90, A0000_2A9B, A0000_2AA9, A0000_2ABF, A0000_29D6, A0000_29DF, A0000_3865}
        { A0000_3898, A0000_38D3, A0000_1B40, A0000_3C59, A0001_7559}
        subgraph clusterTextBox {
            label="Text Boxen"
            { A0000_30E8, A0000_1922, A0001_72EA, A0001_734C, A0001_735A, A0001_7367, A0000_36A0}
        }
    }
    subgraph clusterMenu {
        label="Menus";
        subgraph clusterMenuParty {
            label="Party Menu";
            { A0004_72ED, A0000_3AC2, A0000_13FC, A0000_1420, A0000_145A, A0004_6CD2, A0000_14D4, A0000_14D9} 
            { A0000_14DC, A0004_6CE3}
        }
        subgraph clusterMenuStart {
            label="Start Menu";
            { A0000_2B70, A0000_2ACD, A0000_2ADF}
        }
        subgraph clusterMenuOption {
            label="Option Menu";
            { A0001_5E8A, A0001_601F, A0001_604C}
        }
        { A0001_5AF2, A0000_3ABE, A0000_3BF9, A0000_3BEC }
    }
    subgraph clusterVideo {
        label="Video";
        subgraph clusterVideoSprite {
            label="Sprites";
            { A0000_2841, A0000_5057, A0000_2877, A0000_2897, A0001_50AD, A0001_50BD, A0001_50DC, A0000_2429}
            { A0001_4C34, A0001_4C54, A0000_28C4, A0000_24FD, A0000_251A, A0000_3533, A0000_3541, A0000_354E}
            { A0000_2556, A0000_3558, A0001_5157, A0000_363A, A0000_2649, A0000_26BF, A0000_16C2, A0000_26D4}
            { A0000_16EA, A0000_36EB, A0000_27C7, A0000_276D, A0001_5236, A0001_52B7, A0001_52B2, A0001_52BA}
            { A0001_4E31, A0000_1627, A0000_1665, A0000_1384}
            subgraph clusterVideoSpritePlayer {
                label="Player"
                { A0000_104D, A0000_1055, A0000_105D, A0000_1063, A0000_0997}
            }
        }
        subgraph clusterVideoPallete {
            label="Pallete";
        { A0000_20BA, A0000_3DD4, A0000_3DDC, A0000_3DE5, A0000_20D1, A0000_20D8, A0000_20DD, A0000_20EF, A0000_20F6}
        { A0000_20FB}
        }
        { A0000_0061, A0000_007B, A0000_190F, A0000_18C4, A0000_18D6, A0000_3DD7, A0000_20AF, A0000_3739, A0000_18FC}
        { A0000_3090, A0000_09E8}
    }
    subgraph clusterMemory {
        label="Memory"
        { A0000_2004, A0000_0082, A0000_28C4, A0000_16DF, A0000_180D, A0000_182B, A0000_1886, A0000_009D, A0000_00B5}
        { A0000_3913, A0001_4BED, A0000_17F7, A0000_36E0, A0001_42B1, A0000_2670, A0000_268B, A0000_350C}
    }
    subgraph clusterSound {
        label="Sound";
        { A0000_23B1, A0000_0951, A0000_13D0, A0000_200E, A0000_2310, A0000_2324, A0000_23A1, A0000_3740}
    }
    subgraph clusterItem {
        label="Items";
        { A0000_3040, A0000_30BC, A0000_30C4, A0000_30D9, A0001_4DE1, A0000_2BBB, A0000_2BCF, A0000_3493, A0003_6571}
        { A0003_6581, A0003_65B9, A0003_55C7, A0000_3E2E, A0003_4E74, A0003_4E04, A0003_66F1, A0003_6764, A0003_6479}
        { A0000_2FCF, A0000_37DF, A001E_7F86, A0000_2FF3}
        subgraph clusterItemMart {
            label="Mart";
            { A0000_2A2E, A0001_6C20, A0000_2B96, A0000_2B9E, A0001_6DE7, A0001_6DEF, A0001_6DF7, A0000_35A6}
        }
    }
    subgraph clusterBattle {
        label="Battle";
        { A0000_0683, A0000_3354, A0000_32D7}
    }""")
        for addr in procs:
            tags = ''

            info = database.procInfo(addr)

            if info.has_switch:
                tags += ' switch'
            if info.suspicious_switch:
                tags += ' suspicious_switch'
            if info.has_nop:
                tags += ' nop'
            if info.has_ambig_calls:
                tags += ' ambig_calls'
            if info.has_suspicious_instr:
                tags += ' suspicious'

            f.write('    ' + addr_symbol(addr) + ' [label="' + database.nameForAddress(addr) + tags + '"];\n')
            if tags:
                f.write('    ' + addr_symbol(addr) + ' [color="green"];\n')



            """"q = len(procedure.at(addr).instructions)

            if q < 32:
                intensity = 0
            elif q < 128:
                intensity = 64
            elif q < 512:
                intensity = 128
            elif q < 2048:
                intensity = 192
            else:
                intensity = 255
            """
            intensity = 0

            f.write('    ' + addr_symbol(addr) + ' [fillcolor="#FF{0:02x}{0:02x}"];\n'.format(255-intensity))
            f.write('    ' + addr_symbol(addr) + ' [style="filled"];\n')

            for c in info.calls:
                f.write('    ' + addr_symbol(addr) + ' -> ' + addr_symbol(c) + ';\n')
            for c in info.tail_calls:
                f.write('    ' + addr_symbol(addr) + ' -> ' + addr_symbol(c) + ' [color="blue"];\n'
)
        f.write("}\n")

def save_dot_for_bank(database, bank):
    bank_name = '{:04X}'.format(bank)

    with open('data/bank'+bank_name+'.dot', 'w') as f:
        f.write("digraph crossref {\n")

        cur = database.connection.cursor()
        cur.execute('select addr from procs where substr(addr, 0, 5)=?', (bank_name,))
        for proc_result in cur.fetchall():
            addr = address.fromConventional(proc_result[0])
            tags = ''

            info = database.procInfo(addr)

            is_public = False

            for c in info.callers:
                if c.bank() != bank:
                    is_public = True

            if info.has_switch:
                tags += ' switch'
            if info.suspicious_switch:
                tags += ' suspicious_switch'
            if info.has_nop:
                tags += ' nop'
            if info.has_ambig_calls:
                tags += ' ambig_calls'
            if info.has_suspicious_instr:
                tags += ' suspicious'

            if tags:
                f.write('    ' + addr_symbol(addr) + ' [color="green"];\n')

            if is_public:
                tags += ' public'

            f.write('    ' + addr_symbol(addr) + ' [label="' + database.nameForAddress(addr) + tags + '"];\n')
            f.write('    ' + addr_symbol(addr) + ' [style="filled"];\n')

            for c in info.calls:
                if c.bank() == bank:
                    f.write('    ' + addr_symbol(addr) + ' -> ' + addr_symbol(c) + ';\n')
            for c in info.tail_calls:
                if c.bank() == bank:
                    f.write('    ' + addr_symbol(addr) + ' -> ' + addr_symbol(c) + ' [color="blue"];\n')
        cur.close()
        f.write("}\n")

def produce_map(proj, ownership):

    granularity = 4
    romsize = 512*1024
    width = 64
    height = romsize/granularity/width

    img = Image.new('RGB', (width, height))

    for i in range(romsize/granularity):
        owners = set()
        for j in range(i*granularity, (i+1)*granularity):
            addr = address.fromPhysical(j)
            owners |= ownership[addr]

        color = (0, 0, 0)
        addr = address.fromPhysical(i*granularity)
        if len(owners) == 1:
            color = (0, 255, 0)
        elif len(owners) >= 2:
            color = (255, 0, 0)
        elif addr.bank() in (0x08, 0x0C, 0x0D, 0x0E, 0x0F, 0x10, 0x11, 0x12, 0x13, 0x1C, 0x1D):
            color = (0, 0, 255)
        elif addr.bank() == 0x16 and addr.virtual() >= 0x5700:
            color = (0, 0, 255)
        elif addr.bank() == 0x09 and addr.virtual() >= 0x6700:
            color = (0, 0, 255)
        elif proj.rom.get(addr) == 0xFF:
            color = (0, 0, 127)

        x = i % width
        y = i / width
        img.putpixel((x, y), color)

    img.save('ownership.png')
    print('image saved')


def getSubgraph(database, start_points):
    queue = set(start_points)
    verts = set()

    while queue:
        x = queue.pop()
        if x in verts:
            continue

        verts.add(x)
        info = database.procInfo(x)
        for c in info.calls:
            queue.add(c)
    return verts

def search(proj):
    """
    input = [
address.fromConventional("0003:6A4B"),
address.fromConventional("0019:4461"),
address.fromConventional("0003:66BF"),
address.fromConventional("0018:7B61"),
address.fromConventional("0003:69C9"),
address.fromConventional("0003:5397"),
address.fromConventional("0003:52BE"),
address.fromConventional("0007:7AE3"),
address.fromConventional("0018:7930"),
address.fromConventional("0003:5844"),
address.fromConventional("0003:6A3D"),
address.fromConventional("0003:5882"),
address.fromConventional("0003:6AE7"),
address.fromConventional("0006:79CD"),
address.fromConventional("0004:7E6B"),
address.fromConventional("0006:7547"),
address.fromConventional("0004:5C04"),
address.fromConventional("0004:5BFF"),
address.fromConventional("0004:5C04"),
#address.fromConventional("0003:5A35"),
address.fromConventional("0007:785E"),
address.fromConventional("0006:797B"),
address.fromConventional("0006:6641"),
address.fromConventional("0006:6641"),
address.fromConventional("0006:7470"),
address.fromConventional("0006:673C"),
address.fromConventional("0006:4ACE"),
address.fromConventional("0006:7CFC"),
address.fromConventional("0006:7CD0"),
address.fromConventional("0015:4EAB"),
address.fromConventional("0006:7F5F"),
address.fromConventional("0006:4F5D"),
address.fromConventional("0006:7727"),
address.fromConventional("0006:65FB"),
address.fromConventional("0006:7EB5"),
address.fromConventional("0003:50B4"),
#address.fromConventional("0003:4D1E"),
#address.fromConventional("0003:4D1E"),
address.fromConventional("0006:760B"),
address.fromConventional("0019:6765"),
address.fromConventional("0004:5A8B"),
address.fromConventional("0004:6C2B"),
address.fromConventional("0015:75E5"),
address.fromConventional("0007:76BC"),
address.fromConventional("0003:5D7F"),
address.fromConventional("0003:60C0"),
address.fromConventional("0003:617D"),
address.fromConventional("0003:5CD0"),
address.fromConventional("0003:5BDC"),
address.fromConventional("0003:5BCB"),
address.fromConventional("0003:5BB0"),
address.fromConventional("0003:5BA0"),
address.fromConventional("0003:5A9C"),
address.fromConventional("0003:5A39"),
address.fromConventional("0003:609D"),
address.fromConventional("0003:5FEE"),
address.fromConventional("0003:5DDA"),
address.fromConventional("0003:5D92"),
address.fromConventional("0003:6083"),
address.fromConventional("0003:6029"),
address.fromConventional("0003:5FFF"),
address.fromConventional("0005:4DE5"),
address.fromConventional("0005:4915"),
address.fromConventional("0005:47E1"),
address.fromConventional("0006:6801"),
address.fromConventional("0018:5E68"),
address.fromConventional("0015:4494"),
address.fromConventional("0015:443F"),
address.fromConventional("0015:4365"),
address.fromConventional("0015:40FD"),
address.fromConventional("0015:41C7"),
address.fromConventional("0015:423A"),
address.fromConventional("0015:42AD"),
address.fromConventional("0003:5395"),
address.fromConventional("0004:7679"),
address.fromConventional("0004:762B"),
address.fromConventional("0004:6E46"),
address.fromConventional("0006:7AB3"),
address.fromConventional("0004:6971"),
address.fromConventional("0004:67E6"),
address.fromConventional("0004:67E6"),
address.fromConventional("0004:5F59"),
address.fromConventional("0004:7D80"),
address.fromConventional("0004:7C90"),
address.fromConventional("0004:5DE9"),
address.fromConventional("0004:5EF7"),
address.fromConventional("0004:569D"),
address.fromConventional("0004:5072"),
address.fromConventional("0004:49C1"),
address.fromConventional("0004:4009"),
address.fromConventional("0005:6C41"),
address.fromConventional("0005:7B05"),
address.fromConventional("0007:694D"),
address.fromConventional("0005:67CD"),
address.fromConventional("0019:4216"),
address.fromConventional("0005:6261"),
address.fromConventional("0005:59BB"),
address.fromConventional("0018:5DEF"),
address.fromConventional("0005:54AA"),
address.fromConventional("0015:4324"),
address.fromConventional("0005:549F"),
address.fromConventional("0015:7458"),
address.fromConventional("0018:53C2"),
address.fromConventional("0005:529E"),
address.fromConventional("0018:5D8B"),
address.fromConventional("0005:452E"),
address.fromConventional("0005:4038"),
address.fromConventional("0006:6BB4"),
address.fromConventional("0019:4894"),
address.fromConventional("0006:6248"),
address.fromConventional("0006:60C3"),
address.fromConventional("0006:60C3"),
address.fromConventional("0006:6248"),
address.fromConventional("0018:4DBF"),
address.fromConventional("0018:4CA4"),
address.fromConventional("0018:4B33"),
address.fromConventional("0006:5CE8"),
address.fromConventional("0006:5ABE"),
address.fromConventional("0006:5C4E"),
address.fromConventional("0006:5D5C"),
address.fromConventional("0006:5EFD"),
address.fromConventional("0006:62DE"),
address.fromConventional("0006:63CD"),
address.fromConventional("0006:642A"),
address.fromConventional("0018:72C6"),
address.fromConventional("0006:6A88"),
address.fromConventional("0006:6C58"),
address.fromConventional("0006:6ED4"),
address.fromConventional("0006:7066"),
address.fromConventional("0006:71C9"),
address.fromConventional("0006:7339"),
address.fromConventional("0006:7C19"),
address.fromConventional("0006:56B5"),
address.fromConventional("0006:53A1"),
address.fromConventional("0006:5107"),
address.fromConventional("0006:5049"),
address.fromConventional("0006:5049"),
address.fromConventional("0006:4EBF"),
address.fromConventional("0006:4F36"),
address.fromConventional("0006:4B92"),
address.fromConventional("0019:4777"),
address.fromConventional("0006:4949"),
address.fromConventional("0006:4247"),
address.fromConventional("0006:451B"),
address.fromConventional("0006:4150"),
address.fromConventional("0007:70AD"),
address.fromConventional("0006:4020"),
address.fromConventional("0019:5AFD"),
address.fromConventional("0019:4805"),
address.fromConventional("0007:7503"),
address.fromConventional("0007:7444"),
address.fromConventional("0007:7314"),
address.fromConventional("0007:71B4"),
address.fromConventional("0007:715E"),
address.fromConventional("0019:4022"),
address.fromConventional("0007:7031"),
address.fromConventional("0007:63F1"),
address.fromConventional("0007:6525"),
address.fromConventional("0007:666D"),
address.fromConventional("0007:61FB"),
address.fromConventional("0007:60BD"),
address.fromConventional("0007:60BD"),
address.fromConventional("0007:6198"),
address.fromConventional("0007:5F54"),
address.fromConventional("0007:5B47"),
address.fromConventional("0007:5D87"),
address.fromConventional("0007:597C"),
address.fromConventional("0019:680A"),
address.fromConventional("0019:680A"),
address.fromConventional("0019:687E"),
address.fromConventional("0007:55D5"),
address.fromConventional("0007:53DC"),
address.fromConventional("0007:52C6"),
address.fromConventional("0007:5109"),
address.fromConventional("0007:4F03"),
address.fromConventional("0015:751C"),
address.fromConventional("0007:4A88"),
address.fromConventional("0007:4CA8"),
address.fromConventional("0007:49A3"),
address.fromConventional("0007:480D"),
address.fromConventional("0007:44D3"),
address.fromConventional("0007:4272"),
address.fromConventional("0018:772B"),
address.fromConventional("0018:77EA"),
address.fromConventional("0007:4015"),
address.fromConventional("0018:6FA8"),
address.fromConventional("0018:69C7"),
address.fromConventional("0018:64A7"),
address.fromConventional("0018:6362"),
address.fromConventional("0018:627D"),
address.fromConventional("0018:6176"),
address.fromConventional("0018:5EB6"),
address.fromConventional("0018:4000"),
address.fromConventional("0018:54F7"),
address.fromConventional("0015:73C9"),
address.fromConventional("0015:734E"),
address.fromConventional("0018:451D"),
address.fromConventional("0018:5298"),
address.fromConventional("0018:50FC"),
address.fromConventional("0018:4E40"),
address.fromConventional("0018:49F5"),
address.fromConventional("0015:44BD"),
address.fromConventional("0019:6B97"),
address.fromConventional("0018:4957"),
address.fromConventional("0019:6E13"),
#address.fromConventional("0018:5132"), #
#address.fromConventional("0018:5180"), # cannot be included until 0018:5168 problems resolved
#address.fromConventional("0018:525D"), #
address.fromConventional("0018:51CA"),
address.fromConventional("0019:5D58"),
address.fromConventional("0019:5918"),
address.fromConventional("0019:5817"),
address.fromConventional("0019:55F3"),
address.fromConventional("0019:56E8"),
address.fromConventional("0019:54C1"),
address.fromConventional("0019:5344"),
address.fromConventional("0019:52E4"),
address.fromConventional("0019:518A"),
address.fromConventional("0019:4C9A"),
address.fromConventional("0019:4A1C"),
address.fromConventional("0019:4527"),
address.fromConventional("0015:768A"),
address.fromConventional("0015:78AC"),
address.fromConventional("0015:4D58"),
address.fromConventional("0015:4BF5"),
address.fromConventional("0015:46BE"),
address.fromConventional("0006:7C19"),
address.fromConventional("0015:5096"),
address.fromConventional("0015:409A"),
address.fromConventional("0017:7547"),
address.fromVirtual(0x100), address.fromVirtual(0x40), address.fromVirtual(0x48)
]
    #input = [address.fromVirtual(0x100), address.fromVirtual(0x40), address.fromVirtual(0x48)]
    """
    input = [
# in 0000:0C40
address.fromConventional("0002:5023"),
address.fromConventional("0002:4D92"),
address.fromConventional("0002:490E"),
address.fromConventional("0002:4D00"),
address.fromConventional("0002:4F30"),
address.fromConventional("0002:50A2"),
address.fromConventional("0002:4EFF"),

# in 0000:0B53
address.fromConventional("0002:5DD5"),
address.fromConventional("0002:5731"),
]

    #database.setInitial(input)

    input = proj.database.getAll()
    #input = database.getUnfinished()

    input = [address.fromConventional("0000:345B")]

    procs = set(input)
    callers = defaultdict(set)
    to_update = list(input)

    for i in range(5000):
        if not to_update:
            break

        x = to_update.pop()

        #if x.bank() in (0x1E, 0x1F, 0x1B):
        #    continue

        proj.flow.refresh(x)

        calls = proj.flow.at(x).calls() | proj.flow.at(x).tailCalls()
        for c in calls:
            callers[c].add(x)
            if c not in procs:
                proj.database.reportProc(c)
                procs.add(c)
                to_update.insert(0, c)

        #affected = set()
        #for c in callers[x]:
        #    if database.procInfo(x).has_ambig_calls:
        #        affected.add(x)
        #to_update = list(affected - set(to_update)) + to_update

    print('saving dot')
    save_dot(proj.database, procs)
    print('saved dot')
