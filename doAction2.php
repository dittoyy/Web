<?php
header('content-type:text/html;charset=utf-8');
require_once 'upload2.class.php';
//print_r($_FILES);
$upload=new upload('myFile','imooc');
$dest=$upload->uploadFile();
echo $dest;
?>