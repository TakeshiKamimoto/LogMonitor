<?php

//データーベースに接続
$con = mysql_connect('localhost', 'USER', 'PASSWORD');
mysql_select_db('DATABASE_NAME');

//データー取得
$sql = "SELECT * FROM temperature_data ORDER BY id LIMIT 100 ;";
$res = mysql_query( $sql );
while( $val = mysql_fetch_assoc( $res ) ){
  $json[] = $val;
}

//jsonで出力
echo json_encode( $json );
