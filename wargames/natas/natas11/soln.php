<?php function xor_encdec($in, $key) {
    $text = $in;
    $outText = '';
    for ($i = 0; $i < strlen($text); $i++) {
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }
    return $outText;
} ?>

<?php
    # This code generates the key from the encoded data and the original data
    $data = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");
    echo "Key (approx.): " . xor_encdec(json_encode($data), base64_decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw="));
?>

<?php
    # This code uses the key to encode the crafted data into the payload payload.
    $data = array( "bgcolor"=>"#ffffff", "showpassword"=>"yes" );
    echo "Payload (base64): data=" . base64_encode(xor_encdec(json_encode($data), "qw8J")) . "=\n";

    #  Once the payload is echoed, set javascript:document.cookie="${payload}",
    #  and reload the page.
?>
