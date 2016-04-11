package messagequeue;

import com.rabbitmq.client.*;
import java.io.*;
import java.util.*;

public class Worker {

  private static final String TASK_QUEUE_NAME = "task_queue";
<<<<<<< HEAD
  private static final String TASK_QUEUE_NAME1 = "sinker";
=======
  private static final String TASK_QUEUE_NAME1 = "sinkering";
>>>>>>> 091525ef6d107575ed0496fd2eca1efda7e25fab
  
  public static void main(String[] argv) throws Exception {
    ConnectionFactory factory = new ConnectionFactory();
    factory.setHost("192.168.43.128");
    factory.getSaslConfig();
    final Connection connection = factory.newConnection();
    final Channel channel = connection.createChannel();

    channel.queueDeclare(TASK_QUEUE_NAME, true, false, false, null);
    System.out.println(" [*] Waiting for messages. To exit press CTRL+C");

    channel.basicQos(1);

    final Consumer consumer = new DefaultConsumer(channel) {
      @Override
      public void handleDelivery(String consumerTag, Envelope envelope, AMQP.BasicProperties properties, byte[] body) throws IOException {
        CronDecodeInterface c = new CronImplementation();
        ByteArrayInputStream bais = new ByteArrayInputStream(body);
        DataInputStream in = new DataInputStream(bais);
        ArrayList<String> dbEvent = new ArrayList(); //converting data from client to MAP
        while (in.available() > 0) {
            String element = in.readUTF();
            dbEvent.add(element);
        }
        System.out.println(dbEvent.size());
        Map<String, Integer> seussCount = c.countEvent(dbEvent);
        Map<String, Integer> sortedMap = c.sortByComparator(seussCount);
        
        ByteArrayOutputStream byteOut = new ByteArrayOutputStream();
        ObjectOutputStream out = new ObjectOutputStream(byteOut);
        out.writeObject(sortedMap);
        byte[] bytes = byteOut.toByteArray();
        channel.queueDeclare(TASK_QUEUE_NAME1, true, false, false, null);
        channel.basicPublish("", TASK_QUEUE_NAME1,
                MessageProperties.PERSISTENT_TEXT_PLAIN,
                bytes);
      }
    };
    channel.basicConsume(TASK_QUEUE_NAME, false, consumer);
  }

}