<?php
$a = readline();
$b = explode(" ", readline());
$c = explode(" ", readline());

foreach($b as $elem){
    echo ($elem * $a) . ' ';
}

echo "\n";

foreach($c as $elem){
    $x .= ($elem * $a) . ' ';
}

rtrim($x);
echo $x;

?>