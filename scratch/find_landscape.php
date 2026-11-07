<?php
$html = file_get_contents('c:/xampp/htdocs/luci/scratch/luccimedia.html');
preg_match_all('/([a-zA-Z0-9_-]+\/292551\/[a-zA-Z0-9_\-\.]+\.(?:jpg|jpeg|png))/i', $html, $matches);
$imgs = array_unique($matches[0]);

echo "Checking " . count($imgs) . " images...\n";
$opts = ['http' => ['header' => "User-Agent: Mozilla/5.0\r\n"]];
$ctx = stream_context_create($opts);

$landscape = [];
foreach ($imgs as $rel) {
    $url = 'https://static.showit.co/1200/' . $rel;
    // Download first 32KB to get dimensions
    $headers = @get_headers($url, true);
    if (!$headers) continue;
    $data = @file_get_contents($url, false, $ctx, 0, 65536);
    if (!$data) continue;
    $size = @getimagesizefromstring($data);
    if ($size) {
        $w = $size[0];
        $h = $size[1];
        $ratio = $w / max(1, $h);
        echo basename($rel) . " -> {$w}x{$h} (ratio: " . round($ratio, 2) . ")\n";
        if ($ratio > 1.3) {
            $landscape[] = ['url' => $url, 'file' => basename($rel), 'w' => $w, 'h' => $h, 'ratio' => $ratio];
        }
    }
}

file_put_contents('scratch/landscape_imgs.json', json_encode($landscape, JSON_PRETTY_PRINT));
echo "Found " . count($landscape) . " landscape images.\n";

