package college;

  
public class Admission{
    public static void main(String[] args)
    {
        Student stud = new Student(1,"kanchan","female",2);
        Student stud1 = new Student(2,"kamalesh","male",3);
        stud.printpretty();
        stud1.printpretty();
    }
}