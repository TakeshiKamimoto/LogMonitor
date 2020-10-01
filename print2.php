<?php

//データーベースに接続
$con = new PDO("sqlite:/home/pi/LogMonitor/measure.db");

//
$sql = "SELECT timestamp,temp,temp_m,humid,humid_m,press,press_m,discomfort FROM weather WHERE timestamp>datetime('now','-16 hour')";
$res = $con->query($sql);

while( $val = $res->fetch(PDO::FETCH_ASSOC) ){
  $json[] = $val;
}

//jsonで出力
echo json_encode( $json );
