<?php
//open connection to mysql db
$connection = mysqli_connect("localhost","root","","scraper") or die("Error " . mysqli_error($connection));

//fetch table rows from mysql db
$sql = "select * from monitor WHERE status='Open' ORDER BY id DESC";
$result = mysqli_query($connection, $sql) or die("Error in Selecting " . mysqli_error($connection));


echo "<table border='0.5' >
<tr>
<td align=center width=10%><b>#</b></td>
<td align=center width=35%><b>Type</b></td>
<td align=center width=40%><b>Command</b></td>
<td align=center width=35%><b>Status</b></td></td>";
$i=1;
while($data = mysqli_fetch_row($result))
    if ($i<=10){
        {   
            echo "<tr>";
            echo "<td align=center width=10%>$i</td>";
            echo "<td align=center width=35%>$data[1]</td>";
            echo "<td align=center width=40%>$data[2]</td>";
            echo "<td align=center width=35%>$data[3]</td>";
            echo "</tr>";
        }
    $i++;
    }
echo "</table>";


mysqli_close($connection);
?>