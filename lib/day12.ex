defmodule Day12 do
  import Helpers
  
  def parse_line(line) do
    pat = ~r/^(?<dir>N|S|E|W|L|R|F{1})(?<val>[[:digit:]]+)$/
    %{"dir"=>dir, "val"=>val} = Regex.named_captures(pat, line)
    {dir, elem(Integer.parse(val), 0)}
  end

  def process_directions1([], heading, x_pos, y_pos), do: {heading, x_pos, y_pos}
  def process_directions1([{dir, val} | rest], heading, x_pos, y_pos) do
    {heading, x_pos, y_pos} =
      case dir do
        "L" -> {rem(heading + val, 360), x_pos, y_pos}
        "R" -> {rem(heading - val + 360, 360), x_pos, y_pos}
        "F" ->
          case heading do
            0 -> {heading, x_pos + val, y_pos}
            90 -> {heading, x_pos, y_pos + val}
            180 -> {heading, x_pos - val, y_pos}
            270 -> {heading, x_pos, y_pos - val}
          end
        "N" -> {heading, x_pos, y_pos + val}
        "S" -> {heading, x_pos, y_pos - val}
        "E" -> {heading, x_pos + val, y_pos}
        "W" -> {heading, x_pos - val, y_pos}
      end
    process_directions1(rest, heading, x_pos, y_pos)             
  end
  
  def part1(input) do
    parsed_input = read_lines(input, &parse_line/1)
    {heading, x_pos, y_pos} = process_directions1(parsed_input, 0, 0, 0)
    IO.inspect({heading, x_pos, y_pos})
    abs(x_pos) + abs(y_pos)
  end

  def rotate_left(0, x_pos, y_pos), do: {x_pos, y_pos}
  def rotate_left(90, x_pos, y_pos), do: {-y_pos, x_pos}
  def rotate_left(180, x_pos, y_pos), do: {-x_pos, -y_pos}
  def rotate_left(270, x_pos, y_pos), do: {y_pos, -x_pos}
  
  def process_directions2([], waypt_x, waypt_y, x_pos, y_pos), do: {waypt_x, waypt_y, x_pos, y_pos}
  def process_directions2([{dir, val} | rest], waypt_x, waypt_y, x_pos, y_pos) do
    IO.inspect({waypt_x, waypt_y, x_pos, y_pos})
    IO.inspect({dir, val})
    {waypt_x, waypt_y, x_pos, y_pos} =
      case dir do
        "L" ->
          {waypt_x, waypt_y} = rotate_left(val, waypt_x, waypt_y)
          {waypt_x, waypt_y, x_pos, y_pos}
        "R" ->
          {waypt_x, waypt_y} = rotate_left(360 - val, waypt_x, waypt_y)
          {waypt_x, waypt_y, x_pos, y_pos}
        "F" ->
          {waypt_x, waypt_y, val * waypt_x + x_pos, val * waypt_y + y_pos}
        "N" -> {waypt_x, waypt_y + val, x_pos, y_pos}
        "S" -> {waypt_x, waypt_y - val, x_pos, y_pos}
        "E" -> {waypt_x + val, waypt_y, x_pos, y_pos}
        "W" -> {waypt_x - val, waypt_y, x_pos, y_pos}
      end
    process_directions2(rest, waypt_x, waypt_y, x_pos, y_pos)             
  end
  
  def part2(input) do
    parsed_input = read_lines(input, &parse_line/1)
    {waypt_x, waypt_y, x_pos, y_pos} = process_directions2(parsed_input, 10, 1, 0, 0)
    IO.inspect({waypt_x, waypt_y, x_pos, y_pos})
    abs(x_pos) + abs(y_pos)
  end

end
