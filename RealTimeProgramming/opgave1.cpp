#include <iostream>
#include <unistd.h>
#include <iostream>
#include "Timer.h"
#include <thread>

using namespace std;

class Werker{
   public:
   void doeIets(char c,unsigned int tijd,unsigned int aantal) 
   {      
      for(int i=0;i<aantal;++i) 
      {
         cout<<c<<flush;       //flush leeg output buffer (print direct)
         usleep(100000*tijd);
      }
      cout<<endl;
   }
};

int main() {
   
  Timer tm1;
  tm1.Reset();
  pid_t pid;
   Werker w1;  
   Werker w2;
   Werker w3;
   Werker w4;
   thread t1(&Werker::doeIets,w1,'p',5,8);
   thread t2(&Werker::doeIets,w2,'a',10,8);
   thread t3(&Werker::doeIets,w3,'b',15,8);
   thread t4(&Werker::doeIets,w4,'c',20,8);
   t1.join();
   t2.join();
   t3.join();
   t4.join();
  tm1.Stop();
  cout<<tm1.deTijd()<<"  "<<tm1.deNtijd()<<endl;
 
   return 0;
}



