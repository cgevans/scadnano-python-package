import scadnano as sc


def create_design() -> sc.Design:
    length = 16
    helices = [sc.Helix(max_offset=length, grid_position=(h, v))
               for v in range(-4, 6) for h in range(-4, 6)]
    design = sc.Design(helices=helices, strands=[], grid=sc.honeycomb)

    return design


if __name__ == '__main__':
    d = create_design()
    d.write_scadnano_file(directory='output_designs')
