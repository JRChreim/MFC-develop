#!/usr/bin/env python3
import math

#Numerical setup
Nx      = 100
dx      = 1./(1.*(Nx+1))
Ny  = 70
dy = 1./(1.*(Ny+1))
Tend    = 0.03
Nt      = 100
mydt    = Tend/(1.*Nt)

# Command to navigate between directories
from os import chdir

# Command to acquire directory path
from os.path import dirname

# Command to acquire script name and module search path
from sys import argv, path

# Navigating to script directory
if len(dirname(argv[0])) != 0: chdir(dirname(argv[0]))

# Adding master_scripts directory to module search path
mfc_dir = '../../src'; path[:0] = [mfc_dir + '/master_scripts']

# Command to execute the MFC components
from m_python_proxy import f_execute_mfc_component

# Serial or parallel computational engine
engine = 'serial'
# ==============================================================================

# Case Analysis Configuration ==================================================

# Selecting MFC component
comp_name = argv[1].strip()

# Configuring case dictionary
case_dict =                                                                     \
    {                                                                           \
                    # Logistics ================================================
                    'case_dir'                     : '\'.\'',                   \
                    'run_time_info'                : 'F',                       \
                    'nodes'                        : 1,                         \
                    'ppn'                          : 1,                         \
                    'queue'                        : 'normal',                  \
                    'walltime'                     : '24:00:00',                \
                    'mail_list'                    : '',                        \
                    # ==========================================================
                                                                                \
                    # Computational Domain Parameters ==========================
                    'x_domain%beg'                 : 0.E+00,                    \
                    'y_domain%beg'                 : 0.E+00,                    \
                    'x_domain%end'                 : 1.E+00,                    \
                    'y_domain%end'                 : 1.E+00,                    \
                    'm'                            : Nx,                        \
                    'n'                            : Ny,                         \
                    'p'                            : 0,                         \
                    'dt'                           : mydt,                      \
                    't_step_start'                 : 0,                         \
                    't_step_stop'                  : int(Nt),                   \
                    't_step_save'                  : int(Nt),                   \
                    # ==========================================================
                                                                                \
                    # Simulation Algorithm Parameters ==========================
                    'num_patches'                  : 1,                         \
                    'model_eqns'                   : 2,                         \
                    'alt_soundspeed'               : 'F',                       \
                    'num_fluids'                   : 1,                         \
                    'adv_alphan'                   : 'T',                       \
                    'mpp_lim'                      : 'F',                       \
                    'mixture_err'                  : 'F',                       \
                    'time_stepper'                 : 1,                         \
                    'weno_vars'                    : 2,                         \
                    'weno_order'                   : 5,                         \
                    'weno_eps'                     : 1.E-16,                    \
                    'mapped_weno'                  : 'T',                       \
                    'null_weights'                 : 'F',                       \
                    'mp_weno'                      : 'F',                       \
                    'riemann_solver'               : 2,                         \
                    'wave_speeds'                  : 1,                         \
                    'avg_state'                    : 2,                         \
                    'bc_x%beg'                     : -1,                        \
                    'bc_y%beg'                     : -1,                        \
                    'bc_x%end'                     : -1,                        \
                    'bc_y%end'                     : -1,                        \
                    # ==========================================================
                                                                                \
                    # Formatted Database Files Structure Parameters ============
                    'format'                       : 1,                         \
                    'precision'                    : 2,                         \
                    'prim_vars_wrt'                :'T',                        \
                    'parallel_io'                  :'T',                        \
                    # ==========================================================
                                                                                
                    # Patch 1 L ================================================
                    # 'patch_icpp(1)%geometry'       : 1,                         \
                    # 'patch_icpp(1)%x_centroid'     : 0.25,                      \
                    # 'patch_icpp(1)%length_x'       : 0.5,                       \
                    # 'patch_icpp(1)%vel(1)'         : 0.0,                       \
                    # 'patch_icpp(1)%pres'           : 1.0,                       \
                    # 'patch_icpp(1)%alpha_rho(1)'   : 1.E+00,                    \
                    # 'patch_icpp(1)%alpha(1)'       : 1.,                        \
                    # # ==========================================================

                    # Patch 2 R ================================================
                    # 'patch_icpp(2)%geometry'       : 1,                         \
                    # 'patch_icpp(2)%x_centroid'     : 0.75,                      \
                    # 'patch_icpp(2)%length_x'       : 0.5,                       \
                    # 'patch_icpp(2)%vel(1)'         : 0.0,                       \
                    # 'patch_icpp(2)%pres'           : 0.1,                       \
                    # 'patch_icpp(2)%alpha_rho(1)'   : 0.125E+00,                 \
                    # 'patch_icpp(2)%alpha(1)'       : 1.,                        \
                    # ==========================================================

                    # Patch 1D Analytical ======================================
                    'patch_icpp(1)%geometry'       : 7,
                    \
                    'patch_icpp(1)%x_centroid'     : 0.5,                       \
                    'patch_icpp(1)%y_centroid'     : 0.5,                       \
                    'patch_icpp(1)%length_x'       : 1.0,                       \
                    'patch_icpp(1)%length_y'       : 1.0,                       \
                    'patch_icpp(1)%vel(1)'         : 0.05,                      \
                    'patch_icpp(1)%vel(2)'         : 0.05,                      \
                    'patch_icpp(1)%pres'           : 1.1,                       \
                    'patch_icpp(1)%alpha_rho(1)'   : 1.E+00,                    \
                    'patch_icpp(1)%alpha(1)'       : 1.,                        \
                    # ==========================================================


                    # Fluids Physical Parameters ===============================
                    'fluid_pp(1)%gamma'            : 1.E+00/(1.4-1.E+00),       \
                    'fluid_pp(1)%pi_inf'           : 0.0,                       \
                    # ==========================================================
    }

# Executing MFC component
f_execute_mfc_component(comp_name, case_dict, mfc_dir, engine)

# ==============================================================================
