Hi Alan,

I am copying the installer to
\\fsg54ykf\IT_Desktop_Software_Tools\Public\CommVault-Good-Test

You will need to copy this locally.  To install you will need to install from a command line (with administrative rights).
The command line will look like the one below, but you will need to change it in order for the paths to match

C:\ProgramData\CommmVaultInst\64Bit\WinX64\setup.exe /Silent /Play "C:\windows\ccmcache\af\resources\64Bit\WinX64\install.xml"

For instance, if you copy this to c:\CV then your command line would be
C:\CV\64Bit\WinX64\setup.exe /Silent /Play " C:\CV\64Bit\WinX64\install.xml"

The installer is silent, but will take a few minutes to complete.  I haven’t confirmed, but probably removing the /silent argument will give you verbose mode.

There are several backup servers in use, but this installation will perform the backups on server bkp38cnc.rim.net.

Again though, I suspect that without rimnet access, you won’t be able to complete the backups.

Let me know how it goes
