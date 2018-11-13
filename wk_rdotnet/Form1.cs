using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using RDotNet;

namespace wk_rdotnet
{
    public partial class Form1 : Form
    {
        private RDotNet.REngine Engine = null;

        private void runPrint(SymbolicExpression obj)
        {
            var func = Engine.Evaluate("print").AsFunction();
            func.Invoke(new SymbolicExpression[] { obj });
        }

        public Form1()
        {
            InitializeComponent();

            string R_HOME = System.Environment.GetEnvironmentVariable("R_HOME");

            if (!R_HOME.EndsWith("\\"))
            {
                R_HOME += "\\";
            }

            REngine.SetEnvironmentVariables(R_HOME + "bin\\x64", R_HOME);
            Engine = REngine.GetInstance();
            
            Console.WriteLine("REngine is initialized.");
        }

        private void exampleOfNumericMatrixToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var mat = Engine.Evaluate("mat <- matrix(1:100, nrow=10)").AsNumericMatrix();
            Console.WriteLine("----------");
            Console.WriteLine("Example of NumericVector.");
            Console.WriteLine("----------");
            Console.WriteLine("Type of mat : ");
            Console.WriteLine(mat.GetType());
        }

        private void exampleOfNumericVectorToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var vec = Engine.Evaluate("vec <- rnorm(1000)").AsNumeric();
            var hst = Engine.Evaluate("hst <- hist(vec)").AsList();
            Console.WriteLine("----------");
            Console.WriteLine("Example of NumericVector.");
            Console.WriteLine("----------");
            Console.WriteLine("Result of hist() : ");
            runPrint(hst);
            runPrint(hst["counts"]);
        }

        private void exampleOfDataFrameToolStripMenuItem_Click(object sender, EventArgs e)
        {
            string dn = Environment.CurrentDirectory;

            if (!dn.EndsWith("\\"))
            {
                dn += "\\";
            }

            string fn = dn + "example.csv";
            var csv = Engine.Evaluate("csv <- read.csv('" + fn.Replace("\\", "/") + "', stringsAsFactors=F)").AsDataFrame();
            Console.WriteLine("----------");
            Console.WriteLine("Example of DataFrame.");
            Console.WriteLine("----------");
            Console.WriteLine("Name : ");
            runPrint(csv["Name"]);
            Console.WriteLine("Height : ");
            runPrint(csv["Height"]);
        }

        private void exampleOfFunctionToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var func = Engine.Evaluate("func <- function(var){ var + 10 }").AsFunction();
            var vec = Engine.Evaluate("vec2 <- c(1, 2, 3, 4, 5, 6, 7, 8, 9)").AsVector();
            var ret = func.Invoke(new SymbolicExpression[] { vec }).AsNumeric();
            Console.WriteLine("----------");
            Console.WriteLine("Example of Function.");
            Console.WriteLine("----------");
            Console.WriteLine("ret : ");
            runPrint(ret);
        }
    }
}
