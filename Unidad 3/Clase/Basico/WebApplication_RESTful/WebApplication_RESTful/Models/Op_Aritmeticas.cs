using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace WebApplication_RESTful.Models
{
    public class Op_Aritmeticas
    {

        private int _a;
        private int _b;
        private int _tipo_operacion;
        
        
        public int A
        {
            get => _a;
            set => _a = value;
        }

        public int B
        {
            get => _b;
            set => _b = value;
        }

        public int Tipo_operacion
        {
            get => _tipo_operacion;
            set => _tipo_operacion = value;
        }

        public Op_Aritmeticas(int a, int b, int tipo_operacion) {
            A = a;
            B = b;
            Tipo_operacion = tipo_operacion;
        }

        public double getResultado() {
            switch (Tipo_operacion) {
                case 1:
                    return A + B;                    
                case 2:
                    return A - B;                    
                case 3:
                    return A * B;                    
                case 4:
                    return A / B;                    
                default:
                    return 0;
            }        
        }



    }
}