defmodule Day13 do

  def parse_input(input) do
    [tstamp, buses] = String.split(input, "\n")
    {elem(Integer.parse(tstamp), 0), Enum.map(Enum.filter(String.split(buses, ","), &(&1 != "x")), &(elem(Integer.parse(&1), 0)))}
  end

  def parse_input2(input) do
    [tstamp, buses] = String.split(input, "\n")
    buses = for {bus, increment} <- Enum.zip(String.split(buses, ","), 0..100), bus != "x", do: {elem(Integer.parse(bus), 0), increment}
    {elem(Integer.parse(tstamp), 0), buses}
  end
  
  def find_bus(tstamp, buses) do
    bus = Enum.find(buses, &(rem(tstamp, &1) == 0)) 
    if bus, do: {tstamp, bus}, else: find_bus(tstamp+1, buses)
  end

  def find_bus2_brute_force(tstamp, buses) do
    if Enum.all?(buses, fn {id, inc} -> rem(tstamp + inc, id) == 0 end),
      do: tstamp,
      else: find_bus2_brute_force(tstamp+1, buses)
  end

  def find_bus2(current, _, []), do: current
  def find_bus2(current, step, [{bus, increment}|rest]) do
    # IO.inspect({current, step, [{bus, increment}|rest]})
    if rem(current + increment, bus) == 0,
      do: find_bus2(current, step * bus, rest),
      else: find_bus2(current + step, step, [{bus, increment}|rest])
  end
  
  def part1(input) do
    {tstamp, buses} = parse_input(input)
    {departure_tstamp, bus_id} = find_bus(tstamp, buses)
    {tstamp, departure_tstamp, bus_id, (departure_tstamp - tstamp) * bus_id}
  end

  def part2(input) do
    {tstamp, buses} = parse_input2(input)
    IO.inspect({tstamp, buses})
    [{first_bus, 0}|rest] = buses
    find_bus2(0, first_bus, rest)
  end
end
