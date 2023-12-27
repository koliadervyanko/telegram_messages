import {
  Injectable,
  InternalServerErrorException,
  NotFoundException,
} from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { KeyWordEntity } from './entities/key-word.entity';
import { Repository } from 'typeorm';
import { CreateKeyWordDto } from './dto/create-key-word.dto';

@Injectable()
export class KeyWordService {
  constructor(
    @InjectRepository(KeyWordEntity)
    private repository: Repository<KeyWordEntity>,
  ) {}
  findAll() {
    return `This action returns all keyWord`;
  }
  async findOne(keyWord: string) {
    try {
      const entity = await this.repository.findOneBy({ keyWord });
      if (!entity) {
        throw new NotFoundException('This key word not found');
      }
      return entity;
    } catch (error) {
      throw new InternalServerErrorException(`Error: ${error}`);
    }
  }

  async create(createKeyWordDto: CreateKeyWordDto) {
    try {
      return await this.repository.save(createKeyWordDto);
    } catch (error) {
      throw new InternalServerErrorException(`Error: ${error}`);
    }
  }
}
