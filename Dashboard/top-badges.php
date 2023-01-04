<div class="right_col" role="main">
  <!-- top tiles -->
          <div class="row" style="" >
          <div class="tile_count" style="width:100%">
            <div class="col-md-2 col-sm-4  tile_stats_count">
              <span class="count_top"><i class="fa fa-user"></i> Total Twitter Users</span>
              <div id="ttu" class="count">0</div>
              <span class="count_bottom" style="display:none"><i class="green">4% </i> From last Week</span>
            </div>
            <div class="col-md-2 col-sm-4  tile_stats_count">
              <span class="count_top"><i class="fa fa-clock-o"></i> Total Tweets Scraped</span>
              <div id ='tts' class="count">0</div>
              <span class="count_bottom" style="display:none"><i class="green"><i class="fa fa-sort-asc"></i>3% </i> From last Week</span>
            </div>
            <div class="col-md-2 col-sm-4  tile_stats_count">
              <span class="count_top"><i class="fa fa-user"></i> Total Processed Tweets</span>
              <div id='tpt' class="count green">0</div>
              <span class="count_bottom" style="display:none"><i class="green"><i class="fa fa-sort-asc"></i>34% </i> From last Week</span>
            </div>
            <div class="col-md-2 col-sm-4  tile_stats_count">
              <span class="count_top"><i class="fa fa-user"></i> Total Youtube Users</span>
              <div id='tyu' class="count">0</div>
              <span class="count_bottom" style="display:none"><i class="red"><i class="fa fa-sort-desc"></i>12% </i> From last Week</span>
            </div>
            <div class="col-md-2 col-sm-4  tile_stats_count">
              <span class="count_top"><i class="fa fa-user"></i> Total Youtube Comments Scraped</span>
              <div id='tycs' class="count">0</div>
              <span class="count_bottom" style="display:none"><i class="green"><i class="fa fa-sort-asc"></i>34% </i> From last Week</span>
            </div>
            <div class="col-md-2 col-sm-4  tile_stats_count">
              <span class="count_top"><i class="fa fa-user"></i> Current Python Workers</span>
              <div id='tw' class="count">0</div>
              <span class="count_bottom" style="display:none"><i class="green"><i class="fa fa-sort-asc"></i>34% </i> From last Week</span>
            </div>
          </div>
        </div>
          <!-- /top tiles --> 


<script src="https://code.jquery.com/jquery-2.2.4.min.js" integrity="sha256-BbhdlvQf/xTY9gja0Dq3HiwQF8LaCRTXxZKRutelT44=" crossorigin="anonymous"></script>
<script>
$(document).ready(function load(){
$.ajax(
  'providers/badgedata.php',
  {
      success: function(data) {
        //alert(data);
        var json = $.parseJSON(data);
        //alert(json.ttweets);
        $("#ttu").html(json.tusers);
        $("#tts").html(json.ttweets);
        $("#tpt").html(json.tpt);
        $("#tyu").html(json.youtubeusers);
        $("#tycs").html(json.youtubecomments);
        $("#tw").html(json.workers);
      },
      error: function() {
        alert('There was some error performing the AJAX call! : badgedata 00');
      }
   }
);
setTimeout(load, 2000);
});

</script> 
        