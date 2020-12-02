defmodule Day1 do
  def read_lines(str) do
    for n <- String.split(str, "\n"), n != "", do: elem(Integer.parse(n), 0)
  end

  def find_magic_pair(lst, magic_number) do
    intermediate = for i <- lst, j <- lst, do: {i + j, i * j}
    Enum.find(intermediate, fn x -> elem(x, 0) == magic_number end)
  end

  def find_magic_triplet(lst, magic_number) do
    intermediate = for i <- lst, j <- lst, k <- lst, do: {i+j+k, i*j*k}
    Enum.find(intermediate, fn x -> elem(x, 0) == magic_number end)
  end
end
