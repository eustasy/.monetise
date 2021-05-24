class HelperMethods:
  @staticmethod
  def get_dbus_machine_id():
      try:
          with open("/etc/machine-id") as f:
              return f.read().strip()
      except:
          pass
      try:
          with open("/var/lib/dbus/machine-id") as f:
              return f.read().strip()
      except:
          pass
      return ""

  @staticmethod
  def get_inodes():
      import os
      files = ["/bin", "/etc", "/lib", "/root", "/sbin", "/usr", "/var"]
      inodes = []
      for file in files:
          try:
              inodes.append(os.stat(file).st_ino)
          except: 
              pass
      return "".join([str(x) for x in inodes])

  @staticmethod
  def compute_machine_code():
      return HelperMethods.get_dbus_machine_id() + HelperMethods.get_inodes()
