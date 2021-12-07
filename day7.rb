begin
    # Part 1
    text_file = File.open("day7.txt")
    crab_array = text_file.read.split(",")
    sorted_int_crab_array = crab_array.map(&:to_i).sort
    number_of_crab_positions = sorted_int_crab_array.length
    number_of_crab_positions_midpoint = sorted_int_crab_array[number_of_crab_positions / 2]
    part1_sum = []
    for position in sorted_int_crab_array
        part1_sum.append((position - number_of_crab_positions_midpoint).abs)
    end
    puts part1_sum.sum

    # Part 2
    minimum_fuel = number_of_crab_positions * 10000000000000000000000
    for position in sorted_int_crab_array[0] .. sorted_int_crab_array[-1] + 1
        total_fuel = 0
        for crab in sorted_int_crab_array
            steps = (position - crab).abs
            total_fuel = total_fuel + ( steps * (steps + 1) / 2 )
        end
        if total_fuel < minimum_fuel
            minimum_fuel = total_fuel
        end
    end
    puts minimum_fuel
end