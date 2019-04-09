package college;


class student {
    
  private int studentid;
  private String name;
  private String gender;
  private int age;
  student(){}

  student(int studentid,String name,String gender,int age){
        this.studentid = studentid;
        this.name = name;
        this.gender = gender;
        this.age = age; 
  }

  public int Studentid()
  {
    return this.studentid;
  }
  public void Studentid(int value)
  {
    this.studentid = value;
  }

  public String Name()
  {
    return this.name;
  }
  public void Name(String value)
  {
    this.name = value;
  }

  public String Gender()
  {
    return this.gender;
  }
  public void Gender(String value)
  {
    this.gender = value;
  }

  public int Age()
  {
    return this.age;
  }
  public void Age(int value)
  {
    this.age = value;
  }
}