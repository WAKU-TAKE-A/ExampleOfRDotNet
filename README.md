# Example of "R.Net" (for 64bit)

Example of "R.Net" in Ironpython script.  
The library of C# is used. Requires VisualStudio 2017 or higher.

## File

* "wk_rdotnet_ipy" folder.
  * There are IronPython script files.
  * Run "example.py".
* "wk_rdotnet.sln"
  * To install "R.NET".
  * To generate "rdotnet" package.

## Notes on execution

* Open "wk_rdotnet.sln".
* Install "R.NET" with NuGet.
* Build.
* Copy the "x64/debug/rdotnet" or "x64/release/rdotnet" folder to IronPython's "Lib" folder.
* Environment variable "IRONPYTHON_HOME" and "R_HOME" required. They are installation location.
* "example.py" and "example.exe" are example program.

```
import rdotnet
import example
example.RunExample()
```
