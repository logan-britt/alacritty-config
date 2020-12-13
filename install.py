import os
import shutil
import platform
import subprocess

# install the config yml file to the right place on the system
if platform.system() == 'Linux':
  home_path = str(os.path.expanduser('~'))
  config_path = '.config/alacritty/alacritty.yml'
  full_path = str(os.path.join(home_path, config_path))

  # here we run the usual test to see if the folder exsists
  if '.config' in os.listdir(home_path):
    if 'alacritty' in os.listdir(str(os.path.join(home_path, '.config'))):
      shutil.copy('alacritty.yml', full_path)
    
    else:
      new_path = str(os.path.join(home_path, '.config/alacritty'))
      os.mkdir(new_path)

      shutil.copy('alacritty.yml', full_path)

  else:
    _config_path = str(os.path.join(home_path, '.config'))
    os.mkdir(_config_path)

    new_path = str(os.path.join(home_path, '.config/alacritty'))
    os.mkdir(new_path)

    shutil.copy('alacritty.yml', full_path)

elif platform.system() == 'Darwin':
  pass

elif platform.system() == 'Windows':
  pass

else:
  raise RuntimeError('This operating system is not supported!')
