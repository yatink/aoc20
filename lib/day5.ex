defmodule Day5 do
  import Helpers

  def parse_line(line) do
    {row, col} = String.split_at(line, 7)
    {row, _} = row
    |> (&String.replace(&1, "F", "0")).()
    |> (&String.replace(&1, "B", "1")).()
    |> (&Integer.parse(&1, 2)).()
    {col, _} = col
    |> (&String.replace(&1, "R", "1")).()
    |> (&String.replace(&1, "L", "0")).()
    |> (&Integer.parse(&1, 2)).()

    {row, col, row * 8 + col}
  end

  def part1(input),
    do: Enum.max_by(
          read_lines(input, &parse_line/1),
          &(elem(&1, 2)))

  def part2(input) do
    MapSet.difference(
      MapSet.new(1..866),
      Enum.map(
        read_lines(input, &parse_line/1),
        &elem(&1, 2)) |> MapSet.new
    )
  end
end
    
