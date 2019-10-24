public class Queue
{
	private int front;
	private int rear;;
	private int size;
	private int [] arr;

	public Queue(){}
	public Queue(int capacity){
		this.front = 0;
		this.size = 0;
		this.rear = capacity+1;
		this.size= 0;
		this.arr = new int [capacity];
		this.capacity = capacity;

	}
	public int getFrontIndex(){
		return this.front;
	}
	
	public int getRearIndex(){
		return this.rear;
	}

	public int getSize(){
		return this.size;
	}
	
	public boolean isFull(){
		return this.size==this.capacity;
	}
	public boolean isEmpty(){
		return this.size ==0;
	}
	public void enqueue(int item){
		try{
			if(!isFull()){
				this.rear = (this.rear+1) % this.capacity;
				this.arr[this.rear] = item;
				this.size = this.size+1;
				System.out.println(item+" inserted into the stack");
			} else{
				System.out.println("Queue is Full");
			}
		} catch(Exception e){}
	}
	public int dequeue(){
		try{
			if(!isEmpty()){
				this.front = (this.front+1) % this.capacity;
				this.size = this.size-1;
				return this.arr[this.front];
			} else{
				System.out.println("Queue is Empty");
			}
		} catch(Exception e){}
	}
	public static void main(String [] args){
		Queue queue = new Queue(5);
		queue.enqueue(10);
		queue.enqueue(20);
		queue.enqueue(20);
		System.out.println(queue.dequeue());
		System.out.println(queue.dequeue());
		System.out.println(queue.dequeue());
	}
}
