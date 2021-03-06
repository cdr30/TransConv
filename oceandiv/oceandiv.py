"""
Module containing main routines to execute OceanDiv

"""

import parse_args
import namelist
import load
import process
import save
import tools


def main():
    """
    Parse command line arguments and options and run OceanDiv.
    
    """
    # Read options
    args = parse_args.get_args()
    config = namelist.get_namelist(args)
    tools.print_message(config, 'Running OceanDiv...')
    
    # Load data
    tools.print_message(config, 'Loading data...')
    ohcs = load.load_data(config, dtype='ohc')
    flxs = load.load_data(config, dtype='flx')
    basins = load.load_geodata(config, geotype='basins')
    areas = load.load_geodata(config, geotype='areas')

    # Process data 
    ohcs, flxs, basins, areas = process.unify_masks(ohcs, flxs, basins, areas)
    out_cubes = process.process_by_basin(config, ohcs, flxs, basins, areas)
    
    # Save output
    save.save_as_netcdf(config, out_cubes)
    
    # Finished
    tools.print_message(config, 'Finished!')

        
    
