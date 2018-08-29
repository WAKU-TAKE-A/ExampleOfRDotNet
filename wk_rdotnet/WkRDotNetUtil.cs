using System.Collections.Generic;
using System.Linq;
using RDotNet;

namespace wk_rdotnet
{
    public static class WkRDotNetUtil
    {
        public static SymbolicExpression RunFunction(Function func, IList<SymbolicExpression> ops)
        {
            return func.Invoke(ops.ToArray());
        } 
    }
}
