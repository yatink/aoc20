defmodule Day2 do
  import Helpers

  def parse_line(line) do
    {param, passwd} = List.to_tuple(String.split(line, ": "))
    {inputs, char} = List.to_tuple(String.split(param, " "))

    {input1, input2} =
      List.to_tuple(for p <- String.split(inputs, "-"), do: elem(Integer.parse(p), 0))

    {input1, input2, char |> String.to_charlist() |> hd, passwd |> String.to_charlist()}
  end

  def check_password({min, max, char, passwd}) do
    ct = Enum.count(passwd, fn elem -> elem == char end)
    min <= ct and ct <= max
  end

  def xor(input1, input2) do
    (input1 or input2) and not (input1 and input2)
  end

  def check_password2({first, second, char, passwd}) do
    xor(Enum.at(passwd, first - 1) == char, Enum.at(passwd, second - 1) == char)
  end

  def part1(input),
    do:
      Enum.filter(
        read_lines(input, &parse_line/1),
        &check_password/1
      )
      |> Enum.count()

  def part2(input),
    do:
      Enum.filter(
        read_lines(input, &parse_line/1),
        &check_password2/1
      )
      |> Enum.count()
end
