using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;
using WebApplication_RESTful.Models;

namespace WebApplication_RESTful.Controllers
{
    public class OperacionesAritmeticasController : ApiController
    {
        // GET api/OperacionesAritmeticas
        public IEnumerable<int> Get()
        {
            return new int[] { 120, 240, 350 };
        }

        // GET api/OperacionesAritmeticas/5
        public double Get(int a, int b, int tipo_operacion)
        {
            Op_Aritmeticas op;
            op = new Op_Aritmeticas(a, b, tipo_operacion);
            return op.getResultado();
        }

        // POST api/OperacionesAritmeticas
        public double Post([FromBody] int[] vals, int tipo_operacion)
        {
            Op_Aritmeticas op;
            op = new Op_Aritmeticas(vals[0], vals[1], tipo_operacion);
            return op.getResultado();
        }

        // PUT api/OperacionesAritmeticas/5
        public double[] Put([FromBody] double[] vals, double potencia)
        {
            for (int i = 0; i < vals.Length; i++) {
                vals[i] = Math.Pow(vals[i], potencia);
            }
            return vals;
        }

        // DELETE api/OperacionesAritmeticas/5
        public string Delete(int id)
        {
            return "The element with ID = " + id + " was eliminated.";
        }
    }
}
