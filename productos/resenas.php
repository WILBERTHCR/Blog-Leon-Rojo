<?php
// Reseñas de productos León Rojo — auto-publica con filtros anti-spam, sin moderación manual.
header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');
$ADMIN='d5b6dff9fee04296';
$DIR=__DIR__.'/../resenas';
if(!is_dir($DIR)){ @mkdir($DIR,0755,true); @file_put_contents($DIR.'/.htaccess',"Require all denied\nDeny from all\n"); }
function qslug($s){ return preg_match('/^[a-z0-9-]{1,50}$/',(string)$s)?$s:''; }
function qclean($s,$max){ $s=trim(strip_tags((string)$s)); $s=preg_replace('/\s+/u',' ',$s); return mb_substr($s,0,$max); }
function qload($f){ return is_file($f)?(json_decode(file_get_contents($f),true)?:array()):array(); }
function qpub($r){ return array_reverse(array_map(function($x){ unset($x['ip'],$x['t']); return $x; },$r)); }
function qavg($r){ return count($r)?round(array_sum(array_column($r,'rating'))/count($r),1):0; }

$id=qslug(isset($_REQUEST['id'])?$_REQUEST['id']:'');
if(!$id){ http_response_code(400); echo json_encode(array('error'=>'id')); exit; }
$file=$DIR.'/'.$id.'.json';

// Borrado de una reseña (link secreto, por si hay sabotaje)
if(isset($_GET['del']) && isset($_GET['k']) && $_GET['k']===$ADMIN){
  $r=qload($file); $i=(int)$_GET['del'];
  if(isset($r[$i])){ array_splice($r,$i,1); file_put_contents($file,json_encode($r)); }
  echo json_encode(array('ok'=>1,'count'=>count($r))); exit;
}

if($_SERVER['REQUEST_METHOD']==='POST'){
  if(trim(isset($_POST['website'])?$_POST['website']:'')!==''){ echo json_encode(array('ok'=>1)); exit; } // trampa anti-robot
  $author=qclean(isset($_POST['author'])?$_POST['author']:'',40);
  $text=qclean(isset($_POST['text'])?$_POST['text']:'',600);
  $rating=(int)(isset($_POST['rating'])?$_POST['rating']:0);
  if(mb_strlen($author)<2||$rating<1||$rating>5||mb_strlen($text)<4){ http_response_code(400); echo json_encode(array('error'=>'datos')); exit; }
  if(preg_match('#https?://|www\.|\.com|\.net|\.cr\b#i',$text)){ http_response_code(400); echo json_encode(array('error'=>'links')); exit; }
  $ip=hash('sha256',(isset($_SERVER['REMOTE_ADDR'])?$_SERVER['REMOTE_ADDR']:'').'|leonrojo');
  $r=qload($file);
  foreach($r as $x){ if(isset($x['ip'])&&$x['ip']===$ip && (time()-(isset($x['t'])?$x['t']:0))<86400){ http_response_code(429); echo json_encode(array('error'=>'repetida')); exit; } }
  $r[]=array('author'=>$author,'rating'=>$rating,'text'=>$text,'date'=>date('Y-m-d'),'t'=>time(),'ip'=>$ip);
  $fp=fopen($file,'c+'); if($fp){ flock($fp,LOCK_EX); ftruncate($fp,0); fwrite($fp,json_encode($r)); fflush($fp); flock($fp,LOCK_UN); fclose($fp); }
  echo json_encode(array('ok'=>1,'count'=>count($r),'average'=>qavg($r),'reviews'=>qpub($r))); exit;
}

$r=qload($file);
echo json_encode(array('count'=>count($r),'average'=>qavg($r),'reviews'=>qpub($r)));
