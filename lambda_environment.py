#
# These functions retrieve the package list installed in the lambda 
# environment and the environment variables.
#

def listInstalledPackages():
    try:
        import pkg_resources
    except ImportError as error:
        raise ImportError(error)
    
    packageDetails = [ str(pkg).split(' ')) for pkg in pkg_resources.working_set]
    
    print(dict(packagDetails))
        
    return dict(packagDetails)


def listEnvironment():
    try:
        import os
    except ImportError as error:
        raise ImportError(error)
    
    for variable in os.environ.items():
        print(item)

def loadEnvironment():
    try:
        import os
    except ImportError as error:
        raise ImportError(error)
    
    env = {}
    for variable, value in os.environ.items():
        print(variable)
        env[variable] = value
    
    return env
        
    