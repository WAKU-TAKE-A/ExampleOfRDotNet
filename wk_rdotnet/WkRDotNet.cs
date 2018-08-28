using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

// user add
using RDotNet;

namespace wk_rdotnet
{
    public static class WkRDotNet
    {
        private static string r_path = "";
        private static string r_home = "";
        private static REngine _eng = null;

        public static REngine Engine
        {
            get
            {
                return _eng;
            }
        }

        public static void Initialize(string path, string home)
        {
            try
            {
                r_path = path;
                r_home = home;

                REngine.SetEnvironmentVariables(r_path, r_home);
                _eng = REngine.GetInstance();
                _eng.Initialize();

                Console.WriteLine("REngine is initialized.");
            }
            catch (Exception ex_recv)
            {
                throw new ApplicationException(ex_recv.Message);
            }
        }
    }
}
