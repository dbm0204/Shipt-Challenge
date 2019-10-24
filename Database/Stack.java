class Stack {
	private int top;
	private int [] arr;
	private int capacity;


	public Stack(){}
	public Stack(int capacity){
		try{
			this.arr = new int[capacity];
			this.top = -1;
			this.capacity = capacity;
		} catch(Exception e){}
	}
	
	public int getTop(){
		return this.top;
	}
	
	public boolean isFull(){
		return (this.top ==this.capacity);
	}
	
	public boolean isEmpty(){
		return (this.top <0);

	}

	public void push(int item){
		try{
			if (!isFull()){
				arr[++top] = item;
				System.out.println(item+" inserted into stack");
			}else{
				System.out.println("ERROR: Stack reached max capacity");
			}
		} catch (Exception e) {}
	}
	public int pop(){
		try{
			if(!isEmpty()){
				return arr[top--];
			}else{
				System.out.println("ERROR: Stack is Empty");
			}
		} catch(Exception e){}
		return -1;
	}
	public int peek(){
		try{
			if(!isEmpty()){
				return arr[top];
			}else{
				System.out.println("ERROR:Stack is Empty");
			}
		}catch(Exception e){}
		return -1;

	}
	public static void main(String [] args){
		Stack stack = new Stack(5);
		stack.push(10);
		stack.push(20);
		stack.push(30);
		System.out.println("Top of the stack:"+stack.peek());
		System.out.println("Popping Element:"+stack.pop());
		System.out.println("Popping Element:"+stack.pop());
	}
}
