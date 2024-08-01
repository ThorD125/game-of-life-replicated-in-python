
function show($grid) {
    foreach ($row in $grid) {
        foreach ($col in $row) {
            Write-Host "{$col} " -NoNewline
        }
        Write-Host ""
    }
}

function get_location($x, $y) {
    if ($x -lt 0) {
        $x = 0
    }
    if ($x -ge $size_x) {
        $x = $size_x - 1
    }
    if ($y -lt 0) {
        $y = 0
    }
    if ($y -ge $size_y) {
        $y = $size_y - 1
    }
    return ($x, $y)
}

function get_color_location($grid_array, $x, $y) {
    return $grid_array[$y][$x]
}

function count_in_list($list) {
    write-host ")))))))))"
    Write-Host $list
    write-host "-------"
    return counter($list)
}

function get_neighbors($grid_array, $x, $y) {
    $neighbor_list = New-Object Collections.Generic.List[String]

    foreach ($neighbor in $neighbors) {
        $dx, $dy = $neighbor
        $nx, $ny = get_location($x + $dx, $y + $dy)
    
        if (($nx, $ny) -ne ($x, $y)) {
            $new_negihbor = get_color_location -grid_array $grid_array -x $nx -y $ny
            $neighbor_list.Add($new_negihbor)
        }
    
    }
    return count_in_list($neighbor_list)
}
        
function create_evolve_grid($grid_array) {
    $new_grid = New-Object Collections.Generic.List[String]
    foreach ($y in $size_y){
        $row = New-Object Collections.Generic.List[String]
        foreach ($x in $size_x){
            $new_negihbor = get_neighbors($grid_array, $x, $y)
            $row.Add($new_negihbor)
        }
        $new_grid.Add($row)
}
    return $new_grid
}

function count_grid($grid) {
    $count = @{}
    foreach ($char in $chars){
        $count[$char] = 0
        foreach ($row in $grid){
            foreach ($col in $row){
                $count[$col] += 1
            }
        }
    }
    return $count
}

function get_random($chars) {
    return $chars[(Get-Random -Minimum 0 -Maximum $chars.Length)]
}

function generate_grid($size_y, $size_x, $chars) {
    $grid_array = New-Object Collections.Generic.List[String]
    foreach ($y in $size_y){
        $row = New-Object Collections.Generic.List[String]
        foreach ($x in $size_x){
            $char = get_random($chars)
            $row.Add($char)
        }
        $grid_array.Add($row)
    }
    return $grid_array
}

$neighbors = (
    (-1, -1),  
    (-1, 0),  
    (-1, 1),  
    (0, -1),  
    (0, 1),  
    (1, -1),  
    (1, 0),  
    (1, 1)
)

$frames_per_second = 30
$chars = "r -ForegroundColor Red", "g -ForegroundColor Green", "b -ForegroundColor Blue", "y -ForegroundColor Yellow", "o -ForegroundColor DarkGray", "p -ForegroundColor DarkBlue", "c -ForegroundColor Cyan", "m -ForegroundColor Magenta"

$size_x = 50
$size_y = 10

# if (len(sys.argv) > 1){
#     size_x = int(sys.argv[1])
#     size_y = int(sys.argv[2])
# }

$grid_array = generate_grid($size_y, $size_x, $chars)

show($grid_array)

$old_counts = New-Object Collections.Generic.List[String]


show($grid_array)

$frame_duration = 1 / $frames_per_second



while ($true){
    $new_grid = create_evolve_grid($grid_array)
    show($new_grid)
    $grid_array = $new_grid

    $new_count = count_grid($grid_array)
    if ($old_counts -contains $new_count){
        break
    }
    $old_counts.Add($new_count)
    $old_counts = $old_counts[-2..-1]

    Start-Sleep -Seconds $frame_duration
}
