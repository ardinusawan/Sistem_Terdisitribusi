
package messagequeue;

import java.io.*;
import java.util.*;

public class MessageQueue {
    
    public String[] path(int n){
        String p[] = new String[n];
        for(int i=0;i<n;i++){
            if(i==0){
                p[i] ="E:\\ITS\\KULIAH\\SEMESTER 6\\SISTER\\cron\\cron";
            } else{
                p[i] ="E:\\ITS\\KULIAH\\SEMESTER 6\\SISTER\\cron\\cron."+i;
            }
        }
        return p;
    }
    
    public static void main(String[] args) throws IOException, Exception{
        CronDecodeInterface c = new CronImplementation();
//        NewTask n = new NewTask();
//        for(int i=0;i<p.length;i++){
//            File fin = new File(p[i]);
//            ArrayList<String> dbEvent = c.readFile1(fin); //reading file from client
//            n.send(dbEvent, "localhost", i);
//        }
    }
    
}
