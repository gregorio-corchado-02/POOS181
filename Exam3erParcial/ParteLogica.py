from tkinter import messagebox



class ParteLogica:
    def GenerarMatri(self,a,b,c,d,h,i):
      
      r = (a[0]+b[0]+b[1]+c[0]+c[1]+d[2]+d[3]+h[2]+h[3]+i[0]+i[1]+i[2])
      messagebox.showwarning("El resultado es: ",r)
