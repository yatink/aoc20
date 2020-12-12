defmodule Day7 do
  import Helpers

  def parse_line(line) do
    [outer, inner] = String.split(String.replace(line, "bags", "bag"), "contain ")
    outer_bag_pattern = ~r/^(?<colour>[[:print:]]+) bag[s]?/
    outer = Regex.named_captures(outer_bag_pattern, outer)
    inner_bag_pattern = ~r/^(?<num>[[:digit:]]+) (?<colour>[[:print:]]+)bag[.]?$/
    inner = Enum.map(
      String.split(inner, ","),
      fn substring -> substring
      |> String.trim
      |> (&Regex.named_captures(inner_bag_pattern, &1)).()
      end
    )
    IO.inspect(label: "stuck")
    unless not is_nil(inner) do
      for x <- inner,do:
      {
        String.trim(Map.get(outer, "colour")),
        String.trim(Map.get(x, "colour"))
      }
    end
  end

  def part1(input) do
    parsed_chunks = List.flatten(read_lines(input, &parse_line/1, false))
    Enum.reduce(
      parsed_chunks, %{},
      fn li, acc -> Map.put(acc, elem(li, 1), case Map.fetch(acc, elem(li, 1)) do
                                                {:ok, x} -> MapSet.put(x, elem(li, 0))
                                                _ -> MapSet.new([elem(li, 0)])
                                              end)
      end
    )
  end
end
