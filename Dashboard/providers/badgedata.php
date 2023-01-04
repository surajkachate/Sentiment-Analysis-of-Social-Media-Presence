<?php include('connect.php');


//finding total no of Twitter users in system
$tusers = 0;
$sql = "SELECT count(*) FROM users";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  //output data of each row
  while($row = $result->fetch_assoc()) {
    $tusers =($row['count(*)']);
  }
} else {
  $tusers = 0;
}

$ttweets = 0;
$sql = "SELECT count(*) FROM tweets";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  //output data of each row
  while($row = $result->fetch_assoc()) {
    $ttweets = $row['count(*)'];
  }
} else {
  $ttweets = 0;
}

$wordkers = 0;
$sql = "SELECT count(*) FROM monitor WHERE `status` = 'Open'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  //output data of each row
  while($row = $result->fetch_assoc()) {
    $wordkers =($row['count(*)']);
  }
} else {
  $wordkers = 0;
}
$rdata['tusers'] = $tusers;
$rdata['ttweets'] = $ttweets;
// yet to dev

$rdata['tpt'] = 0;
$rdata['youtubeusers'] = 0;
$rdata['youtubecomments'] = 0;
//
$rdata['workers'] = $wordkers;
echo json_encode($rdata); 

include('disconnect.php');

?>