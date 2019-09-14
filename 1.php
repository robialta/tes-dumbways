<?php

class School{
    public $name;
    public $year_in;
    public $year_out;
    public $major;

    function __construct($name, $year_in, $year_out, $major){
        $this->name = $name;
        $this->year_in = $year_in;
        $this->year_out = $year_out;
        $this->major = $major;
    }
}

class Biodata{
    private $name;
    private $age;
    private $address; 
    private $hobbies;
    private $is_married;
    private $list_school;
    private $interest_in_coding;

    function __construct($name, $age, $address, $hobbies, $is_married, $list_school, $interest_in_coding){
        $this->name = $name;
        $this->age = $age;
        $this->address = $address;
        $this->hobbies = $hobbies;
        $this->is_married = $is_married;
        $this->list_school = $list_school;
        $this->interest_in_coding = $interest_in_coding;
    }

    // method yang mereturn biodata dalam bentuk array Associative
    function getBiodata(){
        $bio = array('name'=>$this->name, 
                    'age'=>$this->age, 
                    'address'=>$this->address, 
                    'hobbies'=>$this->hobbies, 
                    'is_married'=>$this->is_married, 
                    'list_schools'=>$this->list_school, 
                    'interest_in_coding'=>$this->interest_in_coding);
        return $bio;
    }
}

//Membuat object school sebagai value list school
$sd = new School('SDN BUNGTIANG', "2001", "2006", null);
$mts = new School('MTS BIRRUL WALIDAIN', "2007", "2010", null);
$ma = new School('MA RENSING RAJAK', "20011", "2013", 'IPS');
// membuat data diri
$mybiodata = new Biodata('Robialta bimara suenri', //name
                        24, //sge
                        "Bungtiang, sakra, lombok timur, NTB", //addres
                        Array('Nonton film', 'Bermain', 'Belanja'),//array hobbies 
                        false, //is_married
                        Array($sd, $mts, $ma), //object school array
                        true); //interest_in_code

header("Content-type: application/json");
// menampilkan biodata dalam bentuk json
echo json_encode($mybiodata->getBiodata());

?>