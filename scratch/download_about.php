<?php
$dir = 'c:/xampp/htdocs/luci/assets/about';
if (!is_dir($dir)) mkdir($dir, 0777, true);

$ctx = stream_context_create([
    'http' => [
        'timeout' => 15,
        'user_agent' => 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    ]
]);

$imgUrl = 'https://static.showit.co/800/cKcGlbw9Mxz9KnZVN5Hj9Q/204040/brand_shoot_45_portrait_the_social_agency.jpg';
$dataImg = @file_get_contents($imgUrl, false, $ctx);
if ($dataImg) {
    file_put_contents("$dir/about_portrait.jpg", $dataImg);
    echo "Saved about_portrait.jpg (" . strlen($dataImg) . " bytes)\n";
} else {
    echo "Failed portrait\n";
}

$vidUrl = 'https://static.showit.co/file/CEx2ecKzavllu9zw7rnGBg/204040/copy_09759a28-cf69-4085-91d9-6acd574997ab.mp4';
$dataVid = @file_get_contents($vidUrl, false, $ctx);
if ($dataVid) {
    file_put_contents("$dir/about_clip.mp4", $dataVid);
    echo "Saved about_clip.mp4 (" . strlen($dataVid) . " bytes)\n";
} else {
    echo "Failed clip\n";
}

