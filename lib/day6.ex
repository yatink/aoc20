defmodule Day6 do
  import Helpers

  def parse_line(line), do: line
  |> (&String.to_charlist(&1)).()
  |> (&MapSet.new(&1)).()

  def process_batch1(batch),
    do: Enum.reduce(batch, &MapSet.union(&1, &2)) |> Enum.count

  def process_batch2(batch),
    do: Enum.reduce(batch, &MapSet.intersection(&1, &2)) |> Enum.count
  
  def process_input([], _, acc), do: acc
  def process_input(input, batch_fn, acc) do
    {batch, rest} = Enum.split_while(input, fn x -> not Enum.empty?(x) end)
    update = batch_fn.(batch)
    rest
    |> case do
         [_ | something ] -> process_input(something, batch_fn, acc+update)
         [] -> acc + update
       end
  end

  def part1(input),
    do: process_input(
          read_lines(input, &parse_line/1, false),
          &process_batch1/1,
          0)

  def part2(input),
    do: process_input(
          read_lines(input, &parse_line/1, false),
          &process_batch2/1,
          0)

end
