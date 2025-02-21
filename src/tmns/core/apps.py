#**************************** INTELLECTUAL PROPERTY RIGHTS ****************************#
#*                                                                                    *#
#*                           Copyright (c) 2025 Terminus LLC                          *#
#*                                                                                    *#
#*                                All Rights Reserved.                                *#
#*                                                                                    *#
#*          Use of this source code is governed by LICENSE in the repo root.          *#
#*                                                                                    *#
#**************************** INTELLECTUAL PROPERTY RIGHTS ****************************#
#

#  Python Libraries
import argparse
import logging
import sys
import traceback

def run( main ):
    '''
    Invokes the provided function inside a block.

    This cannot except parameters.  The return argument will be passed to `sys.exit()`.
    '''

    try:
        sys.exit(main())

    except Exception as e:
        logging.error( e )
        if logging.root.level == logging.DEBUG:
            traceback.print_exc()
        sys.exit(1)