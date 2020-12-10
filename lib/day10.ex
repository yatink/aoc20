defmodule Day10 do
  import Helpers

  def parse_line(line), do: elem(Integer.parse(line), 0)

  # [0, 3]
  # [3]

  def prepare_input(input) do
    input = read_lines(input, &parse_line/1)
    input ++ [0, Enum.max(input) + 3]
  end

  def part1(input) do
    [first|rest] = Enum.sort(prepare_input(input))
    differences = Enum.map(
      Enum.zip([first|rest], rest),
      &(elem(&1, 1) - elem(&1, 0)))
    distribution = Enum.group_by(differences, &Function.identity/1)
    counts = for {diff, elems} <- distribution, do: {diff, Enum.count(elems)}, into: %{}
    Map.get(counts, 1) * Map.get(counts, 3)
  end

  def build_map([], acc), do: Map.get(acc, 0)
  def build_map([first|rest], acc) do
    candidates = for {node, num_paths} <- acc, node <= first + 3, do: {node, num_paths}, into: %{}
    build_map(
      rest,
      Map.put(
        candidates,
        first,
        Enum.sum(Map.values(candidates))))
  end
  
  def part2(input) do
    [first|rest] = Enum.sort(prepare_input(input), :desc)
    build_map(rest, %{first => 1}) 
    
  end
end
