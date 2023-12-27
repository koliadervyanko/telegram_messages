import {
  Injectable,
  InternalServerErrorException,
  NotFoundException,
} from '@nestjs/common';
import { CreateLocationDto } from './dto/create-location.dto';
import { InjectRepository } from '@nestjs/typeorm';
import { LocationEntity } from './entities/location.entity';
import { Repository } from 'typeorm';

@Injectable()
export class LocationService {
  constructor(
    @InjectRepository(LocationEntity)
    private repository: Repository<LocationEntity>,
  ) {}
  async findAll() {
    try {
      return await this.repository.find();
    } catch (error) {
      throw new InternalServerErrorException(`Error: ${error}`);
    }
  }

  async create(createLocationDto: CreateLocationDto) {
    try {
      return await this.repository.save(createLocationDto);
    } catch (error) {
      throw new InternalServerErrorException(`Error: ${error}`);
    }
  }
  async findOne(filters: CreateLocationDto) {
    try {
      const location = this.repository.findOneBy(filters);
      if (!location) {
        throw new NotFoundException('Location with this filters not found');
      }
      return location;
    } catch (error) {
      throw new InternalServerErrorException(`Error: ${error}`);
    }
  }
}
