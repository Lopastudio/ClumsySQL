<?php
global $conn;

function from($table) {
    $result = $conn->query("FROM " . $table);
    if (!$result) {
        die("Failed to do FROM");
    }

    return $result;
}

?>