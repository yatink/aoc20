defmodule Day1 do
  import Helpers
  def parse_line(line), do: elem(Integer.parse(line), 0)

  def find_magic_pair(lst, magic_number) do
    intermediate = for i <- lst, j <- lst, do: {i + j, i * j}
    Enum.find(intermediate, fn x -> elem(x, 0) == magic_number end)
  end

  def find_magic_triplet(lst, magic_number) do
    intermediate = for i <- lst, j <- lst, k <- lst, do: {i + j + k, i * j * k}
    Enum.find(intermediate, fn x -> elem(x, 0) == magic_number end)
  end

  def part1(input) do
    lst = read_lines(input, &parse_line/1)
    find_magic_pair(lst, 2020)
  end

  def part2(input) do
    lst = read_lines(input, &parse_line/1)
    find_magic_triplet(lst, 2020)
  end
end
