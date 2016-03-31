package messagequeue;

import java.util.*;
import java.io.*;
import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;
import com.rabbitmq.client.MessageProperties;

public class NewTask {

  private static final String TASK_QUEUE_NAME = "task_queue";
    
  public static void send(String host, ArrayList<String> data) throws Exception{
      ConnectionFactory factory = new ConnectionFactory();
      factory.setHost(host);
      Connection connection = factory.newConnection();
      Channel channel = connection.createChannel();
      
      ByteArrayOutputStream baos = new ByteArrayOutputStream();
      DataOutputStream out = new DataOutputStream(baos);
        for (String element : data) {
            out.writeUTF(element);
        }
        byte[] bytes = baos.toByteArray();
        channel.queueDeclare(TASK_QUEUE_NAME, true, false, false, null);
        channel.basicPublish("", TASK_QUEUE_NAME,
                MessageProperties.PERSISTENT_TEXT_PLAIN,
                bytes);
        channel.queueDelete(TASK_QUEUE_NAME);
        channel.close();
        connection.close();
  }
  
  public static void main(String[] argv) throws Exception {
        CronDecodeInterface c = new CronImplementation();
        messagequeue.MessageQueue m = new messagequeue.MessageQueue();
        String p[] = m.path(34);
        ArrayList<String> ar = new ArrayList();
        ArrayList<String> ar1 = new ArrayList();
        
        for(int i=0;i<34;i++){
            c.readFile1(new File(p[i]), ar);
            System.out.println(" [x] Sent '" + p[i] + "'");
        }
        System.out.println(ar.size());
        System.out.println(ar1.size());
        int x = ar.size()+ar1.size();
        System.out.println(x);
        send("localhost", ar);
      }
}