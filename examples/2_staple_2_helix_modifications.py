import scadnano as sc
import modifications as mod
import dataclasses

def create_design() -> sc.Design:
    stap_left_ss1 = sc.Domain(1, True, 0, 16)
    stap_left_ss0 = sc.Domain(0, False, 0, 16)
    stap_right_ss0 = sc.Domain(0, False, 16, 32)
    stap_right_ss1 = sc.Domain(1, True, 16, 32)
    scaf_ss1_left = sc.Domain(1, False, 0, 16)
    scaf_ss0 = sc.Domain(0, True, 0, 32)
    scaf_ss1_right = sc.Domain(1, False, 16, 32)
    stap_left = sc.Strand([stap_left_ss1, stap_left_ss0])
    stap_right = sc.Strand([stap_right_ss0, stap_right_ss1])
    scaf = sc.Strand([scaf_ss1_left, scaf_ss0, scaf_ss1_right], color=sc.default_scaffold_color)
    strands = [scaf, stap_left, stap_right]
    design = sc.Design(strands=strands, grid=sc.square)
    design.add_deletion(helix=0, offset=11)
    design.add_deletion(helix=0, offset=12)
    design.add_deletion(helix=0, offset=24)
    design.add_deletion(helix=1, offset=12)
    design.add_deletion(helix=1, offset=24)
    design.add_insertion(helix=0, offset=29, length=1)
    design.add_insertion(helix=1, offset=2, length=1)
    design.assign_dna(scaf, 'AACT' * 16)

    # biotin_mod_5p = dataclasses.replace(mod.biotin_5p, font_size=30)
    # cy3_mod_3p = dataclasses.replace(mod.cy3_3p, font_size=30)

    stap_left.set_modification_5p(mod.biotin_5p)
    stap_left.set_modification_3p(mod.cy3_3p)
    stap_left.set_modification_internal(9, mod.cy3_int)
    stap_left.set_modification_internal(10, mod.biotin_int)
    stap_left.set_modification_internal(11, mod.cy3_int)
    stap_left.set_modification_internal(12, mod.cy5_int)
    stap_left.set_modification_internal(4, mod.cy3_int)
    stap_left.set_modification_internal(26, mod.cy5_int)

    stap_right.set_modification_5p(mod.cy5_5p)
    stap_right.set_modification_internal(5, mod.cy3_int)
    stap_right.set_modification_3p(mod.biotin_3p)

    scaf.set_modification_5p(mod.biotin_5p)
    scaf.set_modification_3p(mod.cy3_3p)
    scaf.set_modification_internal(5, mod.cy5_int)
    scaf.set_modification_internal(32, mod.cy3_int)

    return design


if __name__ == '__main__':
    d = create_design()
    d.write_scadnano_file(directory='output_designs')
